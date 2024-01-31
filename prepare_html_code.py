import os

template = r'''
    <table class="center">
      <tr>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{0}"></video></td>
        <td style="padding-left: 5px; padding-right: 5px;"></td>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{1}"></video></td>
        <td style="padding-left: 5px; padding-right: 5px;"></td>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{2}"></video></td>
        <td style="padding-left: 5px; padding-right: 5px;"></td>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{3}"></video></td>
      </tr>
    </table>
    <center>
      <table class="center">
        <tr>
          <td width=25% style="text-align:center;">"{4}"</td>
          <td style="padding-left: 5px; padding-right: 5px;"></td>
          <td width=25% style="text-align:center;">"{5}"</td>
          <td style="padding-left: 5px; padding-right: 5px;"></td>
          <td width=25% style="text-align:center;">"{6}"</td>
          <td style="padding-left: 5px; padding-right: 5px;"></td>
          <td width=25% style="text-align:center;">"{7}"</td>
        </tr>
      </table>
    </center>'''

template_tail = r'''
    <table class="center">
      <tr>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{0}"></video></td>
        <td style="padding-left: 5px; padding-right: 5px;"></td>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{1}"></video></td>
        <td style="padding-left: 5px; padding-right: 5px;"></td>
        <td><video muted autoplay="autoplay" loop="loop" playsinline src="assets/C2V/{2}"></video></td>
      </tr>
    </table>
    <center>
      <table class="center">
        <tr>
          <td width=25% style="text-align:center;">"{3}"</td>
          <td style="padding-left: 5px; padding-right: 5px;"></td>
          <td width=25% style="text-align:center;">"{4}"</td>
          <td style="padding-left: 5px; padding-right: 5px;"></td>
          <td width=25% style="text-align:center;">"{5}"</td>
        </tr>
      </table>
    </center>'''

input_dir = "assets/C2V"
video_files = os.listdir(input_dir)
video_files = [f for f in video_files if 'useless' not in f]
video_files.sort(key=lambda item: int(item.split('-')[0]))
print(video_files)
i = 0
while i < len(video_files):
    # input("next:")
    files = video_files[i: i+4]
    strs = [f.split('-')[-1].replace('.mp4', '') for f in files]
    inputs = files + strs
    try:
        code = template.format(*inputs)
        print(code)
    except:
        code = template_tail.format(*inputs)
        print(code)
    print()
    i += 4