from django.contrib import admin
from .models import Post, Organization, Hackathon, User, Team, Project, UserTeam, OrgHack, UserTeamHack, UserTeamProject, Role, Skill, Level, UserRole, Speaker, Case, Section, SectionHack, Level

admin.site.register(Post)
admin.site.register(Organization)
admin.site.register(Hackathon)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Project)
admin.site.register(UserTeam)
admin.site.register(OrgHack)
admin.site.register(UserTeamHack)
admin.site.register(UserTeamProject)
admin.site.register(Role)
admin.site.register(Skill)
admin.site.register(UserRole)
admin.site.register(Speaker)
admin.site.register(Case)
admin.site.register(Section)
admin.site.register(SectionHack)
admin.site.register(Level)
