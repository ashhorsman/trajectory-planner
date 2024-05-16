"""Initial migration.

Revision ID: 4671a91c00eb
Revises: 
Create Date: 2024-05-16 12:39:39.612091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4671a91c00eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trajectory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('target_depth', sa.Float(), nullable=False),
    sa.Column('deviation_angle', sa.Float(), nullable=False),
    sa.Column('azimuth', sa.Float(), nullable=False),
    sa.Column('curvature', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trajectory')
    # ### end Alembic commands ###