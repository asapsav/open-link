# Link
We've built interface for discrete communication with a computer, and achieved 96% accuracy on "Yes"/"No" prediciton task (n=100). The device non-invasively reads EMG sygnals around your mouth and decodes it into words.

This repo includes:
1. Sygnal processing and training code "Yes/No" task
2. Sygnal processing and training "8 commands" task
3. Detailed harware BOM and instructions

![Elecrode Placements, A. Kapur](https://github.com/asapsav/Link/blob/a6887b6bd3e9fe57efb003f7cc0613d9f5e2be5c/static/electrode%20placement.png)
## Model
```python
class CustomCNN(nn.Module):
    def __init__(self):
        super(CustomCNN, self).__init__()
        # Assuming the input dimension is (batch_size, channels, height, width)
        self.conv1 = nn.Conv1d(in_channels=6, out_channels=400, kernel_size=12)
        self.pool1 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv1d(in_channels=400, out_channels=400, kernel_size=6)
        self.pool2 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv3 = nn.Conv1d(in_channels=400, out_channels=400, kernel_size=3)
        self.pool3 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv4 = nn.Conv1d(in_channels=400, out_channels=400, kernel_size=3)
        self.pool4 = nn.MaxPool1d(kernel_size=2, stride=2)
        self.conv5 = nn.Conv1d(in_channels=400, out_channels=400, kernel_size=3)
        self.pool5 = nn.MaxPool1d(kernel_size=2, stride=2)

        # Calculate the size of the flattened features after the last pooling layer
        self._to_linear = None
        self.convs = nn.Sequential(self.conv1, nn.ReLU(), self.pool1,
                                   self.conv2, nn.ReLU(), self.pool2,
                                   self.conv3, nn.ReLU(), self.pool3,
                                   self.conv4, nn.ReLU(), self.pool4,
                                   self.conv5, nn.ReLU(), self.pool5)
        self._get_conv_output((6, 1250))  # Example size

        self.fc1 = nn.Linear(self._to_linear, 250)  # The size will depend on the final pooling layer output
        self.drop1 = nn.Dropout(p=0.7)
        self.fc2 = nn.Linear(250, 8)
        self.drop2 = nn.Dropout(p=0.5)

    def _get_conv_output(self, shape):
        # Determine the size of the features after the conv and pooling layers
        with torch.no_grad():
            input = torch.rand(1, *shape)
            output = self.convs(input)
            self._to_linear = output.data.view(1, -1).size(1)

    def forward(self, x):
        # Pass the input through the conv layers
        x = self.convs(x)

        # Flatten the output for the dense layers
        x = x.view(-1, self._to_linear)

        # Pass the output through the dense layers
        x = F.relu(self.fc1(x))
        x = self.drop1(x)
        x = self.fc2(x)
        x = self.drop2(x)

        # Softmax activation for the output
        #x = torch.sigmoid(x) was here for binary problem
        x = F.softmax(x, dim=1)
        return x


class SimpleFNN(nn.Module): # works fine for binary classification problem (96% accuracy on a balances test set)
    def __init__(self, input_size):
        super(SimpleFNN, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x
```
## References
* AlterEgo: A Personalized Wearable Silent Speech Interface. A. Kapur
* Non-Invasive Silent Speech Recognition in Multiple Sclerosis with Dysphonia. Kapur, A



