"""change type of NFE_id to String

Revision ID: 5e8d0e372253
Revises: a4f528912c3b
Create Date: 2022-03-24 01:01:01.555788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e8d0e372253'
down_revision = 'a4f528912c3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nfe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nfe_id', sa.String(), nullable=False),
    sa.Column('date_venc', sa.DateTime(), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('fk_person_provider_nfe', sa.Integer(), nullable=True),
    sa.Column('fk_person_client_nfe', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_person_client_nfe'], ['person.id'], ),
    sa.ForeignKeyConstraint(['fk_person_provider_nfe'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nfe_id')
    )
    op.create_index(op.f('ix_nfe_id'), 'nfe', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_nfe_id'), table_name='nfe')
    op.drop_table('nfe')
    # ### end Alembic commands ###
