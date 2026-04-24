#create pipeline runner to display customers data from txt file using pipeline runner

class PipelineRunner:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)
    def run(self, **kwargs):
        for stage in self.stages:
            data = stage(**kwargs)
        return data