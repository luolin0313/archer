# -*- coding: UTF-8 -*- 

class Const(object):
    workflowStatus = {
        'finish': '已正常结束',
        'abort': '人工终止流程',
        'manreviewing': '等待审核人审核',
        'pass': '审核通过',
        'timingtask': '定时执行',
        'executing': '执行中',
        'autoreviewwrong': '自动审核不通过',
        'exception': '执行有异常',
    }
    # 定时任务id的前缀
    workflowJobprefix = {
        'query': 'query',
        'sqlreview': 'sqlreview',
    }


class WorkflowDict:
    # 工作流申请类型，1.query,2.SQL上线申请
    workflow_type = {
        'query': 1,
        'query_display': '查询权限申请',
        'sqlreview': 2,
        'sqlreview_display': 'SQL上线申请',
    }

    # 工作流状态，0.待审核 1.审核通过 2.审核不通过 3.审核取消
    workflow_status = {
        'audit_wait': 0,
        'audit_wait_display': '待审核',
        'audit_success': 1,
        'audit_success_display': '审核通过',
        'audit_reject': 2,
        'audit_reject_display': '审核不通过',
        'audit_abort': 3,
        'audit_abort_display': '审核取消',
    }
