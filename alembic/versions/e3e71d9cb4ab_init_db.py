"""init db

Revision ID: e3e71d9cb4ab
Revises: 
Create Date: 2022-11-03 23:24:09.192890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3e71d9cb4ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_point',
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_shop_point'))
    )
    op.create_table('customer',
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('shop_point_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shop_point_id'], ['shop_point.id'], name=op.f('fk_customer_shop_point_id_shop_point')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_customer')),
    sa.UniqueConstraint('phone', name=op.f('uq_customer_phone'))
    )
    op.create_table('employee',
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('shop_point_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shop_point_id'], ['shop_point.id'], name=op.f('fk_employee_shop_point_id_shop_point')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_employee')),
    sa.UniqueConstraint('phone', name=op.f('uq_employee_phone'))
    )
    op.create_table('order',
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_point_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('order_type', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name=op.f('fk_order_customer_id_customer')),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], name=op.f('fk_order_employee_id_employee')),
    sa.ForeignKeyConstraint(['shop_point_id'], ['shop_point.id'], name=op.f('fk_order_shop_point_id_shop_point')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order'))
    )
    op.create_table('visit',
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('modified', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('shop_point_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name=op.f('fk_visit_customer_id_customer')),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], name=op.f('fk_visit_employee_id_employee')),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name=op.f('fk_visit_order_id_order')),
    sa.ForeignKeyConstraint(['shop_point_id'], ['shop_point.id'], name=op.f('fk_visit_shop_point_id_shop_point')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_visit'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visit')
    op.drop_table('order')
    op.drop_table('employee')
    op.drop_table('customer')
    op.drop_table('shop_point')
    # ### end Alembic commands ###