"""empty message

Revision ID: 1486d57ddfc5
Revises: aecf3dde19d3
Create Date: 2023-08-10 17:11:08.950730

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1486d57ddfc5'
down_revision = 'aecf3dde19d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('search_result')
    op.drop_table('search_result2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search_result2',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=275), nullable=True),
    sa.Column('link', mysql.TEXT(), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('search_result',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=275), nullable=True),
    sa.Column('link', mysql.TEXT(), nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('image_url', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###