"""empty message

Revision ID: aa718a51876a
Revises: c09e6d6e0774
Create Date: 2023-08-12 14:37:18.642964

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'aa718a51876a'
down_revision = 'c09e6d6e0774'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search_resultf')
    op.drop_table('search_result')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search_result',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=575), nullable=True),
    sa.Column('link', mysql.TEXT(), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=555), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('search_resultf',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
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
