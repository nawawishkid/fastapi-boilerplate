"""init

Revision ID: e6c30d65aee8
Revises: 
Create Date: 2021-05-23 20:27:13.594513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6c30d65aee8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('password', sa.TEXT(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
