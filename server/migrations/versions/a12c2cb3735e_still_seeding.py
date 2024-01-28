"""still seeding..

Revision ID: a12c2cb3735e
Revises: 2ff9f1c68cfd
Create Date: 2024-01-28 18:38:24.869727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a12c2cb3735e'
down_revision = '2ff9f1c68cfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.drop_column('created')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('heroes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###