"""example_migration

Revision ID: 20230919232518
Revises: 
Create Date: 2023-09-19 23:25:19.299081

"""
from pathlib import Path

from alembic import op


# revision identifiers, used by Alembic
revision = '20230919232518'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = Path(f"./app/data/migrations/versions/sqls/{revision}_example_migration/UP.sql")
    op.execute(sqltext=file.read_text())


def downgrade() -> None:
    file = Path(f"./app/data/migrations/versions/sqls/{revision}_example_migration/DOWN.sql")
    op.execute(sqltext=file.read_text())
