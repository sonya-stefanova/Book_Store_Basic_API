"""New Column Added

Revision ID: 406ac0e476b2
Revises: 0d319d55aad5
Create Date: 2024-02-19 01:05:58.558558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '406ac0e476b2'
down_revision: Union[str, None] = '0d319d55aad5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('pages', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'pages')
    # ### end Alembic commands ###