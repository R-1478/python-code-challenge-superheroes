"""still seeding

Revision ID: 2ff9f1c68cfd
Revises: 56aacac22680
Create Date: 2024-01-28 17:21:46.503018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ff9f1c68cfd'
down_revision = '56aacac22680'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('strength',
               existing_type=sa.INTEGER(),
               type_=sa.Enum('Strong', 'Weak', 'Average'),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('strength',
               existing_type=sa.Enum('Strong', 'Weak', 'Average'),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
