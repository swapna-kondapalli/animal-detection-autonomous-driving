import argparse
from fusiongen3d.generator import generate_code

def main():
    parser = argparse.ArgumentParser(description="FusionGen3D: Multi-Modal 3D Object Detection Code Generator")
    parser.add_argument('--modalities', nargs='+', required=True, help='List of sensor modalities (e.g., lidar camera)')
    parser.add_argument('--fusion', type=str, required=True, help='Fusion strategy (e.g., early, mid, late, transformer)')
    parser.add_argument('--dataset', type=str, required=True, help='Dataset name (e.g., KITTI, nuScenes)')
    parser.add_argument('--model', type=str, required=True, help='Model backbone (e.g., TransFusion, PointNet++)')
    args = parser.parse_args()
    generate_code(args.modalities, args.fusion, args.dataset, args.model)

if __name__ == '__main__':
    main()
