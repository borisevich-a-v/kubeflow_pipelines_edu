kubectl delete pods --field-selector status.phase=Failed -n kubeflow
kubectl delete pods --field-selector status.phase=Succeeded -n kubeflow
