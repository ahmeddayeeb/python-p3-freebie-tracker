"""create freebies table

Revision ID: 8ec01d1c9f0f
Revises: 5f72c58bf48c
Create Date: 2025-03-02 17:05:50.722554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec01d1c9f0f'
down_revision = '5f72c58bf48c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'freebies',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('item_name', sa.String()),
        sa.Column('value', sa.Integer()),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id')),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'))
    )


def downgrade() -> None:
    op.drop_table('freebies')
