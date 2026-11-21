# Repository inspection and naming decision

## Inspected baseline

On 2026-11-20 the public repository was `dipteshhh/enterprise-iam-lifecycle-lab`, default branch `main`, with one initial commit (`45ca03a`) and only a two-line README. The clone had no uncommitted work. Its remote was `https://github.com/dipteshhh/enterprise-iam-lifecycle-lab.git`. There were no tracked code references, Pages configuration or reusable Actions to migrate. External consumers and account-level Pages settings were not exhaustively inspected.

## Recommendation

Use **enterprise-identity-security-lab**. It covers governance, authentication, directory services and access security beyond lifecycle automation while retaining an explicit lab identity. Keep the existing repository and history.

Suggested description:

> Hands-on IAM and identity security lab covering SailPoint IdentityIQ, with planned ISC, Active Directory and Entra expansion; governance, RBAC, provisioning and authentication.

The wording deliberately distinguishes the current platform from planned work. The README display title can change before the GitHub slug changes.

## Rename implications and remaining step

No rename has been performed in this foundation. The prompt describes a proposed name and requests an approved rename; keep that URL decision separate from publishing reviewable content. The connected GitHub tools support content delivery but expose no repository rename operation, and local GitHub CLI authentication was invalid during initial inspection.

GitHub normally redirects repository web and Git traffic after a rename, but Pages project URLs and references to hosted Actions need separate attention. Reusing the old repository name can remove the redirect. Review external links and integrations, then rename the existing repository through its Settings page. See [GitHub's rename guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository).

After the rename, update every local clone:

```sh
git remote set-url origin https://github.com/dipteshhh/enterprise-identity-security-lab.git
git remote -v
git fetch origin
```

Then update any hardcoded links, resume/profile references, badges, webhooks and integrations, and verify the new repository URL and the old redirect. Do not create a second repository or force-push history.
