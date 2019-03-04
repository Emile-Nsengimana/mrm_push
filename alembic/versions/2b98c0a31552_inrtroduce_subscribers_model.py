"""inrtroduce subscribers model

Revision ID: 2b98c0a31552
Revises: 4dc4f2425b93
Create Date: 2019-02-21 09:27:43.067615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b98c0a31552'
down_revision = '4dc4f2425b93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('platform', sa.String(), nullable=False),
    sa.Column('subscription_info', sa.String(), nullable=False),
    sa.Column('subscribed', sa.Boolean(), nullable=False),
    sa.Column('subscriber_key', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscriber_calendars',
    sa.Column('subscribers_id', sa.Integer(), nullable=True),
    sa.Column('calendars_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['calendars_id'], ['calendars.id'], ),
    sa.ForeignKeyConstraint(['subscribers_id'], ['subscribers.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscriber_calendars')
    op.drop_table('subscribers')
    # ### end Alembic commands ###