"""empty message

Revision ID: 66daeb700520
Revises: a400ac1a5d5c
Create Date: 2021-03-22 14:15:02.551182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66daeb700520'
down_revision = 'a400ac1a5d5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Property_Information',
    sa.Column('Property_id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=20), nullable=True),
    sa.Column('Number_of_Bedrooms', sa.Integer(), nullable=True),
    sa.Column('Number_of_Bathrooms', sa.Integer(), nullable=True),
    sa.Column('Location', sa.String(length=80), nullable=True),
    sa.Column('Price', sa.Integer(), nullable=True),
    sa.Column('Property_type', sa.String(length=12), nullable=True),
    sa.Column('Description', sa.String(length=80), nullable=True),
    sa.Column('Photo', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('Property_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Property_Information')
    # ### end Alembic commands ###
