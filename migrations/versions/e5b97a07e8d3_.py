"""empty message

Revision ID: e5b97a07e8d3
Revises: 07c479626f6d
Create Date: 2022-08-08 23:51:39.913671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b97a07e8d3'
down_revision = '07c479626f6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.add_column('user', sa.Column('username', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    op.drop_table('people')
    # ### end Alembic commands ###
