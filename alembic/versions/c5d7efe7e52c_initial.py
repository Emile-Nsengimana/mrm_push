"""initial

Revision ID: c5d7efe7e52c
Revises: 
Create Date: 2019-08-28 18:22:51.015957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5d7efe7e52c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channels',
    sa.Column('date_created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('date_updated', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.String(), nullable=False),
    sa.Column('calendar_id', sa.String(), nullable=False),
    sa.Column('resource_id', sa.String(), nullable=False),
    sa.Column('extra_atrributes', sa.String(), nullable=False),
    sa.Column('bouquet_id', sa.Integer(), nullable=True),
    sa.Column('state', sa.Enum('active', 'archived', 'deleted', name='statetype'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('channels')
    # ### end Alembic commands ###
