"""user

Revision ID: 20230924223951
Revises: 
Create Date: 2023-09-24 22:39:51.539832

"""
from pathlib import Path

from alembic import op


# revision identifiers, used by Alembic
revision = "20230924223951"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    file = Path(f"./app/data/migrations/versions/sqls/{revision}_user/UP.sql")
    op.execute(sqltext=file.read_text())


def downgrade() -> None:
    file = Path(
        f"./app/data/migrations/versions/sqls/{revision}_user/DOWN.sql"
    )
    op.execute(sqltext=file.read_text())
