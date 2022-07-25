curl -X POST -n   https://<databricks-instance>/api/2.0/ip-access-lists
curl -X POST -n   https://databricksws-datascience/api/2.0/ip-access-lists
databricks --help
pip install databricks cli
pip install databricks-cli
databricks --help
databricks configure --token
ls
cd clouddrive
ls
cd ..
ls
cd /
ls
cd usr/
ls
cd cloudshell/
ls
cd csuser/
ls
cd ..
databricks fs --help
databricks fs ls
git clone https://github.com/MicrosoftDocs/mslearn-control-authentication-with-apim.git
cd mslearn-control-authentication-with-apim
bash setup.sh
id=$(az sql server list \
    --resource-group terraform-rg \
    --query '[].[id]' \
    --output tsv)
id
az network private-endpoint create     --name sqlPrivateEndpoint     --resource-group databricks-rg     --vnet-name databricksvnet --subnet pe-subnet     --private-connection-resource-id $id     --group-ids sqlServer     --connection-name mysqlConnection
az network private-dns link vnet create     --resource-group viruscantest02-rg     --zone-name "privatelink.database.windows.net"     --name MysqlLink     --virtual-network databricksvnet     --registration-enabled false
az network private-dns link vnet create     --resource-group databricks-rg     --zone-name "privatelink.database.windows.net"     --name MysqlLink     --virtual-network databricksvnet     --registration-enabled false
az network private-endpoint dns-zone-group list
az network dns zone list -g viruscantest02-rg
az network private-dns zone list -g viruscantest02-rg
az network private-dns link vnet create     --resource-group databricks-rg     --zone-name ""/subscriptions/4e32dcdf-a3a4-426d-bdcb-5298a7a6d0b6/resourceGroups/viruscantest02-rg/providers/Microsoft.Network/privateDnsZones/privatelink.database.windows.net" \
    --name MysqlLink \
    --virtual-network databricksvnet \
    --registration-enabled false


terraform init
ls
az logout
exit
RESOURCE_GROUP_NAME=spring-cloud-workshop
SPRING_CLOUD_NAME=azure-spring-cloud-workshop
az spring-cloud create     -g "$RESOURCE_GROUP_NAME"     -n "$SPRING_CLOUD_NAME"     --sku standard
az spring-cloud create -g "$RESOURCE_GROUP_NAME" -n "$SPRING_CLOUD_NAME" --sku standard
az group create -g $RESOURCE_GROUP_NAME -l eastus
az spring-cloud create -g "$RESOURCE_GROUP_NAME" -n "$SPRING_CLOUD_NAME" --sku standard
SPRING_CLOUD_NAME=azure-spring-cloud-workshop25jul22
az spring-cloud create -g "$RESOURCE_GROUP_NAME" -n "$SPRING_CLOUD_NAME" --sku standard
SPRING_CLOUD_NAME=azurespringcld-workshop25jul22
az spring-cloud create -g "$RESOURCE_GROUP_NAME" -n "$SPRING_CLOUD_NAME" --sku standard
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/orgdevendra/springcloud.git
git push -u origin main
git init
git add README.md
git commit -m "first commit"
git branch -M main
git status
