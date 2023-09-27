"""add-token-table

Revision ID: 20230926161031
Revises: 20230924223951
Create Date: 2023-09-26 16:10:31.942442

"""
from pathlib import Path

from alembic import op


# revision identifiers, used by Alembic
revision = "20230926161031"
down_revision = "20230924223951"
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = Path(
        f"./app/data/migrations/versions/sqls/{revision}_add-token-table/UP.sql"
    )
    op.execute(sqltext=file.read_text())


def downgrade() -> None:
    file = Path(
        f"./app/data/migrations/versions/sqls/{revision}_add-token-table/DOWN.sql"
    )
    op.execute(sqltext=file.read_text())
