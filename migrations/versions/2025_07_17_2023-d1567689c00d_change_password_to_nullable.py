"""change password to nullable

Revision ID: d1567689c00d
Revises: cbcea4ed4b3a
Create Date: 2025-07-17 20:23:03.490592

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d1567689c00d"
down_revision: Union[str, None] = "cbcea4ed4b3a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user", "password", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("user", "password", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
