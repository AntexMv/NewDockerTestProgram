FROM python

WORKDIR C:\Python Projects\NewDockerTestProgram

COPY ./ ./

CMD ["python", "NewDockerTestProgram.py"]