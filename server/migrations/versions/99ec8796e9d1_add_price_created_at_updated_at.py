"""add price, created_at, updated_at

Revision ID: 99ec8796e9d1
Revises: 93cc78b32551
Create Date: 2023-09-08 04:17:53.474364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ec8796e9d1'
down_revision = '93cc78b32551'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('price')

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('price')

    # ### end Alembic commands ###
