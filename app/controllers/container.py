from typing import cast

from dependency_injector import containers, providers

from app.controllers.imap.connection import ConnectionManager
from app.controllers.imap.email_processor import EmailProcessor
from app.controllers.imap.listener import IMAPListener
from app.controllers.imap.message_controller import MessageController
from app.repos.container import RepoContainer


class ControllerContainer(containers.DeclarativeContainer):
    repos: RepoContainer = cast(RepoContainer, providers.DependenciesContainer())

    imap_email_processor = providers.Singleton(EmailProcessor, webhook_log_repo=repos.webhook_log)
    imap_connection_manager = providers.Singleton(ConnectionManager)
    imap_message_controller = providers.Singleton(MessageController, connection_manager=imap_connection_manager)
    imap_listener = providers.Singleton(
        IMAPListener,
        connection_health_repo=repos.connection_health,
        uid_tracking_repo=repos.uid_tracking,
        connection_manager=imap_connection_manager,
        email_processor=imap_email_processor,
    )
