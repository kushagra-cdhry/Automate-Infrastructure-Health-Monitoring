FROM public.ecr.aws/lambda/python:3.9

WORKDIR /var/task

COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]
