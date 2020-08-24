#  AWS CloudFormation Scripts

> Demystifying Infrastructure as Code (IaC) on AWS.

![screenshot](./cf_screenshot.png)

Additional description about the project and its features.

## Built With

- AWS CLI
- YAML

## Getting Started

TBD

### Prerequisites

TBD

### Setup

TBD

### Install

TBD

### Usage

TBD

### Deployment

Most of the time it's just:

```
$ aws cloudformation create-stack --stack-name <STACK-NAME> --template-body <FILE-PATH>
```

Other times when providing a local path to a resource that needs to be uploaded to S3 previous to deployment, i.e. the code for a lambda function, CLoudFormation can upload the file to the bucket and replace the path in your file with the path of the file in the bucket.

```
$ aws cloudformation package --template-file <FILE-PATH> --s3-bucket <BUCKET-NAME> --output-template-file <OUTPUT-FILE>

# aws cloudformation deploy --template-file <OUTPUT-FILE> --stack-name <STACK-NAME>
```

## Authors

👤 **Adriaan Beiertz**

- [Github](https://github.com/adriaanbd)
- [Twitter](https://twitter.com/abeiertz)
- [Linkedin](https://linkedin.com/adriaanbd)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](issues/).

## 📝 License

This project is [MIT](lic.url) licensed.
