import volcenginesdkcore
import volcenginesdkdts
import volcenginesdkdts20180101

class DTSClient:
    def __init__(self, region: str = None, ak: str = None, sk: str = None, token: str = None, host: str = None):
        configuration = volcenginesdkcore.Configuration()
        configuration.ak = ak
        configuration.sk = sk
        configuration.session_token = token
        configuration.region = region
        if host is not None:
            configuration.host = host
        volcenginesdkcore.Configuration.set_default(configuration)
        self.openapi_cli = volcenginesdkdts.DTSApi()
        self.openapi_20180101_cli = volcenginesdkdts20180101.DTS20180101Api()

    def describe_transmission_tasks(self, req: volcenginesdkdts.DescribeTransmissionTasksRequest) -> volcenginesdkdts.DescribeTransmissionTasksResponse:
        return self.openapi_cli.describe_transmission_tasks(req)
    
    def create_transmission_task(self, req: volcenginesdkdts.CreateTransmissionTaskRequest) -> volcenginesdkdts.CreateTransmissionTaskResponse:
        return self.openapi_cli.create_transmission_task(req)
    
    def describe_transmission_task_info(self, req: volcenginesdkdts.DescribeTransmissionTaskInfoRequest) -> volcenginesdkdts.DescribeTransmissionTaskInfoResponse:
        return self.openapi_cli.describe_transmission_task_info(req)
    
    def describe_transmission_task_progress(self, req: volcenginesdkdts.DescribeTransmissionTaskProgressRequest) -> volcenginesdkdts.DescribeTransmissionTaskProgressResponse:
        return self.openapi_cli.describe_transmission_task_progress(req)
    
    def modify_transmission_task(self, req: volcenginesdkdts.ModifyTransmissionTaskRequest) -> volcenginesdkdts.ModifyTransmissionTaskResponse:
        return self.openapi_cli.modify_transmission_task(req)
    
    def start_transmission_task(self, req: volcenginesdkdts.StartTransmissionTaskRequest) -> volcenginesdkdts.StartTransmissionTaskResponse:
        return self.openapi_cli.start_transmission_task(req)
    
    def suspend_transmission_task(self, req: volcenginesdkdts.SuspendTransmissionTaskRequest) -> volcenginesdkdts.SuspendTransmissionTaskResponse:
        return self.openapi_cli.suspend_transmission_task(req)
    
    def resume_transmission_task(self, req: volcenginesdkdts.ResumeTransmissionTaskRequest) -> volcenginesdkdts.ResumeTransmissionTaskResponse:
        return self.openapi_cli.resume_transmission_task(req)
    
    def retry_transmission_task(self, req: volcenginesdkdts.RetryTransmissionTaskRequest) -> volcenginesdkdts.RetryTransmissionTaskResponse:
        return self.openapi_cli.retry_transmission_task(req)
    
    def start_transmission_tasks(self, req: volcenginesdkdts.StartTransmissionTasksRequest) -> volcenginesdkdts.StartTransmissionTasksResponse:
        return self.openapi_cli.start_transmission_tasks(req)
    
    def suspend_transmission_tasks(self, req: volcenginesdkdts.SuspendTransmissionTasksRequest) -> volcenginesdkdts.SuspendTransmissionTasksResponse:
        return self.openapi_cli.suspend_transmission_tasks(req)
    
    def resume_transmission_tasks(self, req: volcenginesdkdts.ResumeTransmissionTasksRequest) -> volcenginesdkdts.ResumeTransmissionTasksResponse:
        return self.openapi_cli.resume_transmission_tasks(req)
    
    def retry_transmission_tasks(self, req: volcenginesdkdts.RetryTransmissionTasksRequest) -> volcenginesdkdts.RetryTransmissionTasksResponse:
        return self.openapi_cli.retry_transmission_tasks(req)
    
    def spawn_swimming_lane(self, req: volcenginesdkdts.SpawnSwimmingLaneRequest) -> volcenginesdkdts.SpawnSwimmingLaneResponse:
        return self.openapi_cli.spawn_swimming_lane(req)
    
    def create_subscription_group(self, req: volcenginesdkdts.CreateSubscriptionGroupRequest) -> volcenginesdkdts.CreateSubscriptionGroupResponse:
        return self.openapi_cli.create_subscription_group(req)
    
    def describe_subscription_groups(self, req: volcenginesdkdts.DescribeSubscriptionGroupsRequest) -> volcenginesdkdts.DescribeSubscriptionGroupsResponse:
        return self.openapi_cli.describe_subscription_groups(req)
    
    def update_subscription_group(self, req: volcenginesdkdts.UpdateSubscriptionGroupRequest) -> volcenginesdkdts.UpdateSubscriptionGroupResponse:
        return self.openapi_cli.update_subscription_group(req)
    
    def precheck_async(self, req: volcenginesdkdts20180101.PreCheckAsyncRequest) -> volcenginesdkdts20180101.PreCheckAsyncResponse:
        return self.openapi_20180101_cli.pre_check_async(req)
    
    def get_async_pre_check_result(self, req: volcenginesdkdts20180101.GetAsyncPreCheckResultRequest) -> volcenginesdkdts20180101.GetAsyncPreCheckResultResponse:
        return self.openapi_20180101_cli.get_async_pre_check_result(req)
    
    def add_tags_to_resource(self, req: volcenginesdkdts.AddTagsToResourceRequest) -> volcenginesdkdts.AddTagsToResourceResponse:
        return self.openapi_cli.add_tags_to_resource(req)
    
    def remove_tags_from_resource(self, req: volcenginesdkdts.RemoveTagsFromResourceRequest) -> volcenginesdkdts.RemoveTagsFromResourceResponse:
        return self.openapi_cli.remove_tags_from_resource(req)
    
    def describe_tags_by_resource(self, req: volcenginesdkdts.DescribeTagsByResourceRequest) -> volcenginesdkdts.DescribeTagsByResourceResponse:
        return self.openapi_cli.describe_tags_by_resource(req)
    
    def modify_instance_order(self, req: volcenginesdkdts.ModifyInstanceOrderRequest) -> volcenginesdkdts.ModifyInstanceOrderResponse:
        return self.openapi_cli.modify_instance_order(req)
    
    def create_validation_task(self, req: volcenginesdkdts.CreateValidationTaskRequest) -> volcenginesdkdts.CreateValidationTaskResponse:
        return self.openapi_cli.create_validation_task(req)
    
    def describe_validation_tasks(self, req: volcenginesdkdts.DescribeValidationTasksRequest) -> volcenginesdkdts.DescribeValidationTasksResponse:
        return self.openapi_cli.describe_validation_tasks(req)
    
    def describe_validation_task_info(self, req: volcenginesdkdts.DescribeValidationTaskInfoRequest) -> volcenginesdkdts.DescribeValidationTaskInfoResponse:
        return self.openapi_cli.describe_validation_task_info(req)
    
    def start_validation_task(self, req: volcenginesdkdts.StartValidationTaskRequest) -> volcenginesdkdts.StartValidationTaskResponse:
        return self.openapi_cli.start_validation_task(req)
    
    def suspend_validation_task(self, req: volcenginesdkdts.SuspendValidationTaskRequest) -> volcenginesdkdts.SuspendValidationTaskResponse:
        return self.openapi_cli.suspend_validation_task(req)
    
    def resume_validation_task(self, req: volcenginesdkdts.ResumeValidationTaskRequest) -> volcenginesdkdts.ResumeValidationTaskResponse:
        return self.openapi_cli.resume_validation_task(req)
    
    def retry_validation_task(self, req: volcenginesdkdts.RetryValidationTaskRequest) -> volcenginesdkdts.RetryValidationTaskResponse:
        return self.openapi_cli.retry_validation_task(req)
    
    def start_validation_tasks(self, req: volcenginesdkdts.StartValidationTasksRequest) -> volcenginesdkdts.StartValidationTasksResponse:
        return self.openapi_cli.start_validation_tasks(req)
    
    def suspend_validation_tasks(self, req: volcenginesdkdts.SuspendValidationTasksRequest) -> volcenginesdkdts.SuspendValidationTasksResponse:
        return self.openapi_cli.suspend_validation_tasks(req)
    
    def resume_validation_tasks(self, req: volcenginesdkdts.ResumeValidationTasksRequest) -> volcenginesdkdts.ResumeValidationTasksResponse:
        return self.openapi_cli.resume_validation_tasks(req)
    
    def retry_validation_tasks(self, req: volcenginesdkdts.RetryValidationTasksRequest) -> volcenginesdkdts.RetryValidationTasksResponse:
        return self.openapi_cli.retry_validation_tasks(req)
    
    def download_validation_task_result(self, req: volcenginesdkdts.DownloadValidationTaskResultRequest) -> volcenginesdkdts.DownloadValidationTaskResultResponse:
        return self.openapi_cli.download_validation_task_result(req)
    
    def describe_validation_task_result(self, req: volcenginesdkdts.DescribeValidationTaskResultRequest) -> volcenginesdkdts.DescribeValidationTaskResultResponse:
        return self.openapi_cli.describe_validation_task_result(req)
    
    def get_db_table_diff_details(self, req: volcenginesdkdts.GetDBTableDiffDetailsRequest) -> volcenginesdkdts.GetDBTableDiffDetailsResponse:
        return self.openapi_cli.get_db_table_diff_details(req)
    
    def generate_validation_result_file(self, req: volcenginesdkdts.GenerateValidationResultFileRequest) -> volcenginesdkdts.GenerateValidationResultFileResponse:
        return self.openapi_cli.generate_validation_result_file(req)
    
    def describe_supported_validation_types(self, req: volcenginesdkdts.DescribeSupportedValidationTypesRequest) -> volcenginesdkdts.DescribeSupportedValidationTypesResponse:
        return self.openapi_cli.describe_supported_validation_types(req)
    
    def modify_validation_task(self, req: volcenginesdkdts.ModifyValidationTaskRequest) -> volcenginesdkdts.ModifyValidationTaskResponse:
        return self.openapi_cli.modify_validation_task(req)
    
    def create_data_source(self, req: volcenginesdkdts.CreateDataSourceRequest) -> volcenginesdkdts.CreateDataSourceResponse:
        return self.openapi_cli.create_data_source(req)
    
    def list_data_source(self, req: volcenginesdkdts.ListDataSourceRequest) -> volcenginesdkdts.ListDataSourceResponse:
        return self.openapi_cli.list_data_source(req)
    
    def describe_data_source(self, req: volcenginesdkdts.DescribeDataSourceRequest) -> volcenginesdkdts.DescribeDataSourceResponse:
        return self.openapi_cli.describe_data_source(req)
    
    def modify_data_source(self, req: volcenginesdkdts.ModifyDataSourceRequest) -> volcenginesdkdts.ModifyDataSourceResponse:
        return self.openapi_cli.modify_data_source(req)
    
    def delete_data_source(self, req: volcenginesdkdts.DeleteDataSourceRequest) -> volcenginesdkdts.DeleteDataSourceResponse:
        return self.openapi_cli.delete_data_source(req)
    
    def list_vpc(self, req: volcenginesdkdts20180101.ListVPCRequest) -> volcenginesdkdts20180101.ListVPCResponse:
        return self.openapi_20180101_cli.list_vpc(req)
    
    def list_vpc_subnets(self, req: volcenginesdkdts20180101.ListVPCSubnetsRequest) -> volcenginesdkdts20180101.ListVPCSubnetsResponse:
        return self.openapi_20180101_cli.list_vpc_subnets(req)