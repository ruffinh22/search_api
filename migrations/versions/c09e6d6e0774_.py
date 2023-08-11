"""empty message

Revision ID: c09e6d6e0774
Revises: 70f00ff2c2ac
Create Date: 2023-08-11 05:52:04.387256

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c09e6d6e0774'
down_revision = '70f00ff2c2ac'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('search_resultf',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('text', sa.String(length=2000), nullable=True),  # Specify the length
        sa.Column('images', sa.String(length=2000), nullable=True),  # Specify the length
        sa.Column('post_url', sa.String(length=2000), nullable=True),  # Specify the length
        sa.Column('time', sa.String(length=2000), nullable=True),  # Specify the length
        sa.Column('likes', sa.Integer(), nullable=True),
        sa.Column('comments', sa.Integer(), nullable=True),
        sa.Column('shares', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

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
    op.drop_table('search_resultf')
    # ### end Alembic commands ###
