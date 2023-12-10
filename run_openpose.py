import os
import subprocess
from tqdm import tqdm

root_path = 'c:\\Users\\kevin\\Documents\\Grad\\740\\RWF2000\\openpose\\Datasets\\' # Change to dataset path.
openpose_exe_dir = 'c:\\Users\\kevin\\Documents\\Grad\\740\\RWF2000\\openpose\\bin\\OpenPoseDemo.exe' # Change to openpose.exe path.

def readFromDir(dir, train : bool, fight : bool, tag = None, not_tag = False):
    input_dir = os.path.join(dir, 'train' if train else 'val', 'Fight' if fight else 'NonFight')
    input_videos = os.listdir(input_dir)

    if tag:
        if not_tag:
            input_videos = [v for v in input_videos if tag not in str(v)]
        else:
            input_videos = [v for v in input_videos if tag in str(v)]

    desc = ('train' if train else 'val') + ' ' + ('fight' if fight else 'nonfight')

    output_dir = os.path.join(input_dir, 'OpenPose')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    input_videos = set(input_videos)
    input_videos = input_videos - set(os.listdir(output_dir))
    print(f'{input_dir}: {len(input_videos)}')

    output_videos = [os.path.join(output_dir, v) for v in input_videos]
    input_videos = [os.path.join(input_dir, v) for v in input_videos]
    p_bar = tqdm(enumerate(input_videos), desc=desc)
    for index, input_video in p_bar:
        p_bar.set_description(f'Processing {desc} [{index + 1}/{len(input_videos)}]')
        subprocess.run([
            openpose_exe_dir,
             '--video', input_video,
             '--display', '0',
             '--write_video', output_videos[index],
              '--disable_blending'], cwd='c:\\Users\\kevin\\Documents\\Grad\\740\\RWF2000\\openpose\\') # Change to openpose.exe path.

def main():
    readFromDir(root_path, train=True, fight=False, tag='.avi')
    readFromDir(root_path, train=True, fight=True, tag='.avi')
    readFromDir(root_path, train=True, fight=True, tag='.avi')
    readFromDir(root_path, train=False, fight=False, tag='.avi')


if __name__ =='__main__':
    main()