from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

# Import your Base metadata
from db.models import Base  # Adjust to your actual models module

# Read the Alembic Config object for .ini settings
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set the target metadata for Alembic
target_metadata = Base.metadata

# Retrieve the database URL
DATABASE_URL = config.get_main_option("sqlalchemy.url")


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Create the async engine
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async def do_run_migrations():
        async with connectable.connect() as connection:
            # Configure the migration context
            await connection.run_sync(
                lambda sync_conn: context.configure(
                    connection=sync_conn,
                    target_metadata=target_metadata,
                )
            )
            # Run migrations
            await connection.run_sync(lambda _: context.run_migrations())

    # Use asyncio to run migrations
    import asyncio
    asyncio.run(do_run_migrations())


# Determine whether to run migrations online or offline
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
