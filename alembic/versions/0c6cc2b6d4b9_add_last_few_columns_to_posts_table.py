'''
Author: Mecil Meng
Date: 2022-08-12 15:18:20
LastEditors: Mecil Meng
LastEditTime: 2022-08-12 15:22:52
FilePath: /Full_course/alembic/versions/0c6cc2b6d4b9_add_last_few_columns_to_posts_table.py
Description: 添加posts其它

Copyright (c) 2022 by JCBEL/JCBLE/MSCI/MOTU, All Rights Reserved.
'''
"""add last few columns to posts table

Revision ID: 0c6cc2b6d4b9
Revises: 61a616e8905a
Create Date: 2022-08-12 15:18:20.530109

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0c6cc2b6d4b9'
down_revision = '61a616e8905a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
    )
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
