"""first

Revision ID: 0b35a090a878
Revises: dee91b277e0f
Create Date: 2022-04-01 15:14:20.845683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b35a090a878'
down_revision = 'dee91b277e0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Messages')
    op.drop_table('Admins')
    op.drop_table('admin')
    op.drop_table('Groups')
    op.add_column('Users', sa.Column('ban', sa.Boolean(), nullable=True))
    op.drop_column('Users', 'request_group')
    op.drop_column('Users', 'verified')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('verified', sa.BOOLEAN(), nullable=True))
    op.add_column('Users', sa.Column('request_group', sa.VARCHAR(length=80), nullable=False))
    op.drop_column('Users', 'ban')
    op.create_table('Groups',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('telegram_id', sa.VARCHAR(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('Admins',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('telegram_id', sa.VARCHAR(length=80), nullable=False),
    sa.Column('fullname', sa.VARCHAR(length=80), nullable=False),
    sa.Column('phone', sa.INTEGER(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
