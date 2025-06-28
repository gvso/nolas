# NOlas

A high-performance, async-based headless email client that is Nylas-API compatible.

## 🚀 Key Features

- **Massive Scale**: Handle 1000+ email accounts with 10+ folders each
- **Async Architecture**: Uses asyncio for efficient I/O operations
- **Connection Pooling**: Smart IMAP connection management with rate limiting
- **Distributed Workers**: Horizontal scaling with multiple worker processes
- **Database-Driven**: PostgreSQL for reliable state management
- **Webhook Delivery**: Reliable webhook delivery with retry logic
- **Health Monitoring**: Built-in health checks and automatic recovery
- **Graceful Shutdown**: Clean resource cleanup on shutdown

## 📋 Requirements

- Python 3.13+
- PostgreSQL 12+
- uv for package management (recommended)

## 🛠 Installation

1. **Clone the repository**:

```bash
git clone git@github.com:gvso/nolas.git
cd nolas
```

2. **Install dependencies**:

```bash
uv sync
```

3. **Setup PostgreSQL database**:

```bash
createdb nolas
```

## 🚦 Quick Start

### 1. Add Test Account

Add a test account to verify setup:

```bash
python main.py --mode add-test
```

### 2. List Accounts

View all accounts in the database:

```bash
python main.py --mode list
```

### 3. Start the System

**Production (Cluster Mode)**:

```bash
python main.py --mode cluster --workers 4
```

**Development (Single Worker)**:

```bash
python main.py --mode single
```
