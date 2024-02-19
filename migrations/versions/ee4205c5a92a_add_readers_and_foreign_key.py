"""add readers and foreign key

Revision ID: ee4205c5a92a
Revises: 406ac0e476b2
Create Date: 2024-02-19 01:11:46.484542

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee4205c5a92a'
down_revision: Union[str, None] = '406ac0e476b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('reader_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_books_reader_id'), 'books', ['reader_id'], unique=False)
    op.create_foreign_key(None, 'books', 'readers', ['reader_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_index(op.f('ix_books_reader_id'), table_name='books')
    op.drop_column('books', 'reader_id')
    op.drop_table('readers')
    # ### end Alembic commands ###
