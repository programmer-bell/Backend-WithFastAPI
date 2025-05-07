from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from app.core.config import settings

# 🔧 Set the database URL from your settings
config = context.config
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# 📋 Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 🧠 Import all models to populate Base.metadata
from app.db.base import Base  # <- import Base that reflects all your models
target_metadata = Base.metadata

# 🔌 Offline migrations
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# 🔗 Online migrations
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
