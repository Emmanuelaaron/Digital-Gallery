"""empty message

Revision ID: 1a0e5374ead1
Revises: 
Create Date: 2020-03-30 16:49:41.495706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a0e5374ead1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('basket_reference', sa.String(length=10), nullable=False),
    sa.Column('payment_status', sa.String(length=10), nullable=True),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('kids_tickets', sa.Integer(), nullable=True),
    sa.Column('kidsTicketTotal', sa.Float(), nullable=True),
    sa.Column('adult_tickets', sa.Integer(), nullable=True),
    sa.Column('adultTicketTotal', sa.Float(), nullable=True),
    sa.Column('total_tickets', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('basket_reference')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket_account')
    # ### end Alembic commands ###
