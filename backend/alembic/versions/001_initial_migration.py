"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2024-01-01 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create profiles table
    op.create_table('profiles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('github_url', sa.String(length=255), nullable=True),
        sa.Column('linkedin_url', sa.String(length=255), nullable=True),
        sa.Column('portfolio_url', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profiles_email'), 'profiles', ['email'], unique=True)
    op.create_index(op.f('ix_profiles_id'), 'profiles', ['id'], unique=False)

    # Create skills table
    op.create_table('skills',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_skills_id'), 'skills', ['id'], unique=False)
    op.create_index(op.f('ix_skills_name'), 'skills', ['name'], unique=False)

    # Create projects table
    op.create_table('projects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('links', sa.Text(), nullable=True),
        sa.Column('profile_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_id'), 'projects', ['id'], unique=False)

    # Create work_experiences table
    op.create_table('work_experiences',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('company', sa.String(length=200), nullable=False),
        sa.Column('position', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('start_date', sa.DateTime(), nullable=False),
        sa.Column('end_date', sa.DateTime(), nullable=True),
        sa.Column('profile_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_work_experiences_id'), 'work_experiences', ['id'], unique=False)

    # Create profile_skills association table
    op.create_table('profile_skills',
        sa.Column('profile_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
        sa.PrimaryKeyConstraint('profile_id', 'skill_id')
    )


def downgrade() -> None:
    op.drop_table('profile_skills')
    op.drop_index(op.f('ix_work_experiences_id'), table_name='work_experiences')
    op.drop_table('work_experiences')
    op.drop_index(op.f('ix_projects_id'), table_name='projects')
    op.drop_table('projects')
    op.drop_index(op.f('ix_skills_name'), table_name='skills')
    op.drop_index(op.f('ix_skills_id'), table_name='skills')
    op.drop_table('skills')
    op.drop_index(op.f('ix_profiles_id'), table_name='profiles')
    op.drop_index(op.f('ix_profiles_email'), table_name='profiles')
    op.drop_table('profiles')