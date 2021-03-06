"""migrate to topic

Revision ID: e795091c7b89
Revises: f68c46df9e76
Create Date: 2022-06-05 20:07:56.111422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e795091c7b89'
down_revision = 'f68c46df9e76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.add_column('user', sa.Column('topic', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'topic')
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('field1', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='students_pkey')
    )
    # ### end Alembic commands ###
