"""empty message

Revision ID: 4ec3ad946d58
Revises: ac42e8baa716
Create Date: 2023-08-14 12:07:45.241021

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4ec3ad946d58'
down_revision = 'ac42e8baa716'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search_result')
    op.drop_table('search_resultf')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search_resultf',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=575), nullable=True),
    sa.Column('link', mysql.TEXT(), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=555), nullable=True),
    sa.Column('text', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('images', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('post_url', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('time', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('likes', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comments', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('shares', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('search_result',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=575), nullable=True),
    sa.Column('link', mysql.TEXT(), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=555), nullable=True),
    sa.Column('text', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('images', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('post_url', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('time', mysql.VARCHAR(length=2000), nullable=True),
    sa.Column('likes', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comments', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('shares', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
