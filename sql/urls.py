# -*- coding: UTF-8 -*- 

from django.conf.urls import url

import sql.group
import sql.views_ajax
import sql.workflow
from . import views, views_ajax, query, slowlog, instance, process
from sql.utils import jobs
from sql.utils.config import SysConfig

urlpatterns = [
    url(r'^$', views.sqlworkflow, name='sqlworkflow'),
    url(r'^index/$', views.sqlworkflow, name='sqlworkflow'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^submitsql/$', views.submitSql, name='submitSql'),
    url(r'^editsql/$', views.submitSql, name='editsql'),
    url(r'^submitothercluster/$', views.submitSql, name='submitothercluster'),
    url(r'^sqlworkflow/$', views.sqlworkflow, name='sqlworkflow'),

    url(r'^autoreview/$', views.autoreview, name='autoreview'),
    url(r'^detail/(?P<workflowId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^passed/$', views.passed, name='passed'),
    url(r'^execute/$', views.execute, name='execute'),
    url(r'^timingtask/$', views.timingtask, name='timingtask'),
    url(r'^execute_skipinc/$', views.execute_skipinc, name='execute_skipinc'),
    url(r'^cancel/$', views.cancel, name='cancel'),
    url(r'^rollback/$', views.rollback, name='rollback'),
    url(r'^sqlquery/$', views.sqlquery, name='sqlquery'),
    url(r'^slowquery/$', views.slowquery, name='slowquery'),
    url(r'^sqladvisor/$', views.sqladvisor, name='sqladvisor'),
    url(r'^slowquery_advisor/$', views.sqladvisor, name='slowquery_advisor'),
    url(r'^queryapplylist/$', views.queryapplylist, name='queryapplylist'),
    url(r'^queryapplydetail/(?P<apply_id>[0-9]+)/$', views.queryapplydetail, name='queryapplydetail'),
    url(r'^queryuserprivileges/$', views.queryuserprivileges, name='queryuserprivileges'),
    url(r'^diagnosis_process/$', views.diagnosis_process, name='diagnosis_process'),
    url(r'^diagnosis_sapce/$', views.diagnosis_sapce, name='diagnosis_sapce'),
    url(r'^workflow/$', views.workflows, name='workflows'),
    url(r'^workflowdetail/(?P<audit_id>[0-9]+)/$', views.workflowsdetail, name='workflowsdetail'),
    url(r'^dbaprinciples/$', views.dbaprinciples, name='dbaprinciples'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^config/$', views.config, name='config'),

    url(r'^authenticate/$', views_ajax.authenticateEntry, name='authenticate'),
    url(r'^sqlworkflowlist/$', views_ajax.sqlworkflowlist, name='sqlworkflowlist'),
    url(r'^simplecheck/$', views_ajax.simplecheck, name='simplecheck'),
    url(r'^getMonthCharts/$', views_ajax.getMonthCharts, name='getMonthCharts'),
    url(r'^getPersonCharts/$', views_ajax.getPersonCharts, name='getPersonCharts'),
    url(r'^getOscPercent/$', views_ajax.getOscPercent, name='getOscPercent'),
    url(r'^getWorkflowStatus/$', views_ajax.getWorkflowStatus, name='getWorkflowStatus'),
    url(r'^stopOscProgress/$', views_ajax.stopOscProgress, name='stopOscProgress'),
    url(r'^sqladvisorcheck/$', views_ajax.sqladvisorcheck, name='sqladvisorcheck'),
    url(r'^workflowlist/$', views_ajax.workflowlist, name='workflowlist'),
    url(r'^group_relations/$', sql.group.group_relations, name='group_relations'),
    url(r'^groupauditors/$', sql.group.groupauditors, name='groupauditors'),
    url(r'^changegroupauditors/$', sql.views_ajax.changegroupauditors, name='changegroupauditors'),
    url(r'^changeconfig/$', sql.views_ajax.changeconfig, name='changeconfig'),

    url(r'^getdbNameList/$', instance.getdbNameList, name='getdbNameList'),
    url(r'^getTableNameList/$', instance.getTableNameList, name='getTableNameList'),
    url(r'^getColumnNameList/$', instance.getColumnNameList, name='getColumnNameList'),
    url(r'^getqueryapplylist/$', query.getqueryapplylist, name='getqueryapplylist'),
    url(r'^getuserprivileges/$', query.getuserprivileges, name='getuserprivileges'),
    url(r'^applyforprivileges/$', query.applyforprivileges, name='applyforprivileges'),
    url(r'^modifyqueryprivileges/$', query.modifyqueryprivileges, name='modifyqueryprivileges'),
    url(r'^queryprivaudit/$', query.queryprivaudit, name='queryprivaudit'),
    url(r'^query/$', query.query, name='query'),
    url(r'^querylog/$', query.querylog, name='querylog'),
    url(r'^explain/$', query.explain, name='explain'),
    url(r'^slowquery_review/$', slowlog.slowquery_review, name='slowquery_review'),
    url(r'^slowquery_review_history/$', slowlog.slowquery_review_history, name='slowquery_review_history'),
    url(r'^del_sqlcronjob/$', jobs.del_sqlcronjob, name='del_sqlcronjob'),

    url(r'^process_status/$', process.process_status, name='process_status'),
    url(r'^create_kill_session/$', process.create_kill_session, name='create_kill_session'),
    url(r'^kill_session/$', process.kill_session, name='kill_session'),
]

# if SysConfig().sys_config.get('aliyun_rds_manage') == 'true':
#     from . import aliyun_rds
#
#     aliyun_function_url = [
#         url(r'^process_status/$', aliyun_rds.process_status, name='process_status'),
#         url(r'^sapce_status/$', aliyun_rds.sapce_status, name='sapce_status'),
#         url(r'^create_kill_session/$', aliyun_rds.create_kill_session,
#             name='create_kill_session'),
#         url(r'^kill_session/$', aliyun_rds.kill_session, name='kill_session'),
#     ]
#     urlpatterns.extend(aliyun_function_url)
