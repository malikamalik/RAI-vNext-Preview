# Getting Started with Examples
Before running our samples ensure
1. You have installed the required packages via the [installation instructions]()
2. You have an SKlearn model ready and registered in AzureML and accesss to the data that you used to train the model.
If you are looking for a model to quickstart, [see this sample here from DPv2 private preview](https://github.com/Azure/azureml-previews/tree/main/previews/pipelines/samples/nyc_taxi_data_regression)

|Method | Sample link |Description |
| -- |--|--|
|CLI |0a_boston_housing | Creating a model assessment dashboard using the boston housing dataset |
| Python SDK| | |

## Resources
- [az ml cli v2 documentation](https://docs.microsoft.com/en-us/cli/azure/ml?view=azure-cli-latest)
### Quick reference commands
Login from CLI:
```CLI
az login --tenant <your_tenant_name_such_us_microsoft.onmicrosoft.com>
```
Check defaults set:
```CLI
az configure
```
Set by default Resource Group:
```CLI
az configure --defaults group=<your_resource_group_name> location=<your_azure_region>
```
Set by default AML Workspace:
```CLI
az configure --defaults workspace=<your_workspace_name>

