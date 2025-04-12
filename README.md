# patch-repo
To deploy patches on remote servers

update the patch folder in above git repo

On remote servers:
Pre-requisites:
sudo apt update && sudo apt install -y ansible git python3

For any errors:
python3 --version
sudo ln -s /usr/bin/python3 /usr/bin/python

Command to run:
ansible-pull -U https://github.com/m0hdali18/patch-repo.git -e "schema_name=<schema_name> server_name=localhost jira_id=<patch_id> tomcat_restart=no location=instahms" deploy_patch.yml

For private repo:
git config --global url."https://ghp_AbcDef1234567890ExampleToken@github.com/".insteadOf "https://github.com/"

ansible-pull -U https://github.com/m0hdali18/patch-repo.git \
  -e "schema_name=samirabbas server_name=localhost jira_id=IES-16648 tomcat_restart=no location=instahms" \
  deploy_patch.yml

git config --global --unset-all url."https://<your-token>@github.com/".insteadOf
rm ~/.gitconfig
