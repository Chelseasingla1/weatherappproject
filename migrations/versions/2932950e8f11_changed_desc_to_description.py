"""Changed desc to description

Revision ID: 2932950e8f11
Revises: 
Create Date: 2024-04-29 18:09:49.404988

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2932950e8f11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('robot_commands')
    op.drop_table('usernew')
    op.drop_table('map')
    op.drop_table('user')
    op.drop_table('__EFMigrationsHistory')
    op.drop_table('weathers')
    op.drop_table('robotcommand')
    op.drop_table('maps')
    op.drop_table('mapnew')
    op.drop_table('map_s')
    with op.batch_alter_table('weather', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=200), nullable=False))
        batch_op.drop_column('desc')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weather', schema=None) as batch_op:
        batch_op.add_column(sa.Column('desc', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.drop_column('description')

    op.create_table('map_s',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('columns', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rows', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('createddate', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('modifieddate', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='map_s_pkey')
    )
    op.create_table('mapnew',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('columns', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rows', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('createddate', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('modifieddate', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='mapnew_pkey')
    )
    op.create_table('maps',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('columns', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rows', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='maps_pkey')
    )
    op.create_table('robotcommand',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('Name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=800), autoincrement=False, nullable=True),
    sa.Column('ismovecommand', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('createddate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('modifieddate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_robotcommand')
    )
    op.create_table('weathers',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('city', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('temp', sa.REAL(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='weathers_pkey')
    )
    op.create_table('__EFMigrationsHistory',
    sa.Column('MigrationId', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('ProductVersion', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('MigrationId', name='PK___EFMigrationsHistory')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('passwordhash', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('createddate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('modifieddate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_table('map',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('columns', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rows', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('createddate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('modifieddate', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='map_pkey')
    )
    op.create_table('usernew',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('modified_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='usernew_pkey'),
    sa.UniqueConstraint('email', name='usernew_email_key')
    )
    op.create_table('robot_commands',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_move_command', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('modified_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='robot_commands_pkey')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('role', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('created_date', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('modified_date', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
