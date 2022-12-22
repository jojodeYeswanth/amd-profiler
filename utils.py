
import os
import wrapper_utils
try:
    path = os.path.join(os.getcwd())
    output_path = os.path.join(path, "wrapper")

    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(output_path + " folder created.")

    else:
        print(output_path + " folder already exists.")

    wrapper_utils.data_collector()
    wrapper_utils.rename_workloadfile()
    wrapper_utils.nativePlatformDetails()

    wrapper_utils.tarCreation()

except Exception as e:
    print(e,'exception occured')
