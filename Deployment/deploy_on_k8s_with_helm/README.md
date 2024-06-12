Deploy Dagster on GKE with Helm
==
### Architecture
![alt text](image.png)

Components of Dagster :

- Web server
- Code server
- Daemon
- worker
- Executor
- Database

### Connect cluster

### Build a Docker image for user code
Build an image for user code on Google artifact registry
```bash
gcloud builds submit --timeout "2h" --tag asia-east1-docker.pkg.dev/datapool-1806/data-kubernetes-dev/dagster:1.0.0
```

### Helm

- Make sure Helm 3 installed
```bash
brew install helm
```
- add Dagster into helm repo
```bash
helm repo add dagster https://dagster-io.github.io/helm
```
- Configure your user deployment
    - Configure the deployment
    - Run pod_per_op_job (optional)
  gcloud container clusters get-credentials workflow-orchestrator-poc --zone=asia-east1

請確定有 roles/container.admin 權限 , 若沒有請相關單位執行
stack_overflow:https://github.com/cert-manager/cert-manager/issues/256
refer:https://cloud.google.com/kubernetes-engine/docs/how-to/iam
```bash
gcloud projects add-iam-policy-binding your-project-id --member=user:wiwi_kuo@migocorp.com --role=roles/container.admin
```
並創建 kubernetes ClusterRoleBinding
refer:https://kubernetes.io/docs/reference/access-authn-authz/rbac/
```bash
kubectl create clusterrolebinding wiwi_kuo-cluster-admin-binding --clusterrole=cluster-admin --user=wiwi_kuo@migocorp.com
```

```bash
helm upgrade --install dagster dagster/dagster -f values.yaml 
```
檢視當前所有的 Helm release
```bash
helm list -a
```

reference : https://docs.dagster.io/deployment/guides/kubernetes/deploying-with-helm



$ kubectl create serviceaccount -n default dagster-poc
$ kubectl create clusterrolebinding dagster-cluster-admin-binding  --clusterrole=cluster-admin --serviceaccount default:k8s-digdag-server
$ helm init --service-account --serviceaccount default:k8s-digdag-server