#/usr/bin/env python3
import click
import delegator
import json

@click.command()
def main():
  k8s_ctx = delegator.run('kubectl config current-context').out
  az_ctx = json.loads(delegator.run('az account show').out)

  click.echo('k8s {}'.format(k8s_ctx.strip()))
  click.echo('az {} ({})'.format(az_ctx['name'], az_ctx['id']))

if __name__ == '__main__':
  main()
