# VinJ

**VinJ: An Automated Tool for Large-Scale Software Vulnerability Data Generation**

| | |
|---|---|
| Original artifact | <https://figshare.com/s/faf2c8a24410b34b7e70> |
| Imported from | the publications page |
| Tool | `pubs2github` |


## Other papers sharing this artifact

- VulGen: Realistic Vulnerable Sample Generation via Pattern Mining and Deep Learning
- Generating Vulnerable Code via Learning-Based Program Transformations

---

## Contents

The artifact contains 329 file(s) including Python, Shell scripts, Config files, Data files, and Documentation.

```
├── VulGen
│   ├── devign
│   │   ├── __pycache__
│   │   ├── data_loader
│   │   ├── devign_non_vulgen_reveal
│   │   ├── devign_non_vulgen_xen
│   │   ├── devign_vulgen_gth_reveal
│   │   ├── devign_vulgen_gth_xen
│   │   ├── devign_vulgen_reveal
│   │   ├── devign_vulgen_syn_reveal
│   │   ├── devign_vulgen_syn_xen
│   │   ├── devign_vulgen_xen
│   │   ├── devign_wild_reveal
│   │   ├── devign_wild_xen
│   │   ├── models
│   │   ├── modules
│   │   ├── devign_non_vulgen_reveal.py
│   │   ├── devign_non_vulgen_reveal.sh
│   │   ├── devign_non_vulgen_reveal.txt
│   │   ├── devign_non_vulgen_xen.py
│   │   ├── devign_non_vulgen_xen.sh
│   │   ├── devign_non_vulgen_xen.txt
│   │   ├── devign_vulgen_gth_reveal.py
│   │   ├── devign_vulgen_gth_reveal.sh
│   │   ├── devign_vulgen_gth_reveal.txt
│   │   ├── devign_vulgen_gth_xen.py
│   │   ├── devign_vulgen_gth_xen.sh
│   │   ├── devign_vulgen_gth_xen.txt
│   │   ├── devign_vulgen_reveal.py
│   │   ├── devign_vulgen_reveal.sh
│   │   ├── devign_vulgen_reveal.txt
│   │   ├── devign_vulgen_syn_reveal.py
│   │   ├── devign_vulgen_syn_reveal.sh
│   │   ├── devign_vulgen_syn_reveal.txt
│   │   ├── devign_vulgen_syn_xen.py
│   │   ├── devign_vulgen_syn_xen.sh
│   │   ├── devign_vulgen_syn_xen.txt
│   │   ├── devign_vulgen_xen.py
│   │   ├── devign_vulgen_xen.sh
│   │   ├── devign_vulgen_xen.txt
│   │   ├── devign_wild_reveal.py
│   │   ├── devign_wild_reveal.sh
│   │   ├── devign_wild_reveal.txt
│   │   ├── devign_wild_xen.py
│   │   ├── devign_wild_xen.sh
│   │   ├── devign_wild_xen.txt
│   │   ├── LICENSE
│   │   ├── README.md
│   │   ├── trainer.py
│   │   └── utils.py
│   ├── g2e_vulgen
│   │   ├── __pycache__
│   │   ├── asdl
│   │   ├── common
│   │   ├── datasets
│   │   ├── edit_components
│   │   ├── edit_model
│   │   ├── scripts
│   │   ├── source_data
│   │   ├── trees
│   │   … (159 more items)
│   … (428 more items)
… (431 more items)
```

---

## Original `README.md` (from the upstream artifact)

# VulGen: Realistic Vulnerability Generation Via Pattern Mining and Deep Learning

By combining the strengths of state-of-the-art deterministic (pattern-based) approach for vulnerability injection and probabilisitic (deep-learning/DL-based) program transformation approach for injection localization, we present VulGen, which is the first injection-based vulnerability-generation technique that is not limited to a particular class of vulnerabilities. We compare VulGen with several other possible techniques (T5, Graph2Edit, Getafix) for vulnerability generation and show that VulGen outperforms them.

## Package Structure

- `pattern_mining_applying/`: The source code, evaluation data, and results for pattern mining/applying relevant experiments.
    - `VulGen_beam_1/`: The source code, evaluation data, and results for VulGen evaluation in beam size 1 setting.
        - `generated/`: The VulGen generated functions.
        - `clusters_3000/`: The mined patterns by VulGen.
        - `VulDatasets/`: The dataset we used in for evaluating VulGen and other baseline techniques (**corresponding to the description in Section V.B**).
        - `res.txt`: The testing output of VulGen in beam size 1 setting (**corresponding to Table 1 Row 2 (VulGen) Column 2 (Precision)**).
        `VulRepair_raw_preds_final_beam1.pkl`: The experiment output from the VulGen injection localization model on the testing set (used to localize the statement to inject vulnerability).
        - `testApplying.py` The script to test VulGen using the testing data and generate (possible) vulnerable functions in `generated/`
    - `VulGen_beam_10/`: The source code, evaluation data, and results for VulGen evaluation in beam size 10 setting. The structure is the same as the one in `VulGen_beam_1/`, except:
        - `manual_inspection/`: The manual inspection to compute the vulnerability injection success rate. The files in the `success/` folder are the success functions when randomly sampling 100 functions for manual inspection(**corresponding to Table 1 Row 2 (VulGen) Column 3 (Success Rate)**).
    - `Getafix_beam_1/`: The source code, evaluation data, and results for VulGen evaluation in beam size 10 setting (**corresponding to Table 1 Row 4 (Getafix) Column 2 (Precision)**).  The structure is the same as the one in VulGen_beam_1/
    - `Getafix_beam_10/`: The source code, evaluation data, and results for VulGen evaluation in beam size 10 setting (**corresponding to Table 1 Row 4 (Getafix) Column 3 (Success Rate)**). The structure is the same as the one in VulGen_beam_10/ 
    - `VulGen_wild/`: The source code, evaluation data, and results for VulGen evaluation in beam size 10 setting. The structure is the same as the one in VulGen_beam_1/. **The generated functions in `generated/` are used to improve the vulnerability detection dataset in RQ5**.
- `T5/`: The source code, evaluation data, and results for Transformer-based injection localization and translation experiments.
    - `M1_VulRepair_PL-NL/`: The source code, evaluation data for the experiments. Note that we borrow the source code from [VulRepair](https://github.com/awsm-research/VulRepair). 
        - `T5Train_tokenized_final3/`: The training data for vulnerability injection localization (**see the descriptions in Section IV.B**).
        - `T5Test_tokenized_final3/`: The testing data for vulnerability injection localization (**see the descriptions in Section IV.B**).
        - `T5_vulgen_train_translate_final_tokenized/`: The training data for Transformer-based vulnerability generation baseline approach  (**see the descriptions in Section V.D**).
        - `T5_vulgen_test_translate_final_tokenized/`: The training data for Transformer-based vulnerability generation baseline approach (**see the descriptions in Section V.D**).
        - `saved_models/`: The saved models for T5 relevant experiments (vulnerbility injection localization, Transformer-based vulnerability generation, etc.).
        - `vulrepair_main.py`: The source code for T5 relevant models training and testing.
        - `train.sh`: The script to start training the T5 models.
        - `test.sh`: The script to test the trained T5 models for injection localization or Transformer-based vulnerability generation.
    - `data/raw_predictions/CodeT5/`: The experiment output for Transformer-based injection localization and translation experiments.
        - `VulRepair_raw_preds_final_beam1.csv`: The experiment output for VulGen injection localization model on the testing set in the `VulGen_beam_1/` folder.
        - `VulRepair_raw_preds_final_beam10.csv`: The experiment output for VulGen injection localization model on the testing set in the `VulGen_beam_10/` folder.
        - `VulRepair_raw_preds_wild_beam1.csv`: The experiment output for VulGen injection localization model on the testing set in the `VulGen_wild/` folder.
        - `VulRepair_raw_preds_translate_final_beam10.csv`: The experiment output for Transformer-based vulnerability generation in the beam size 10 setting (**corresponding to Table 1 Row 3 (T5) Column 2 (Precision)**).
        - `VulRepair_raw_preds_translate_final_beam10.csv`: The experiment output for Transformer-based vulnerability generation in the beam size 10 setting (**corresponding to Table 1 Row 3 (T5) Column 3 (Success Rate) experiment**).
    - `manual_inspection_beam_10/`: The manual inspection to compute the vulnerability injection success rate. The files in the `success/` folder are the success functions when randomly sampling 100 functions for manual inspection(**corresponding to Table 1 Row 3 (T5) Column 3 (Success Rate)**).
- `g2e_vulgen/`: The source code, evaluation data, and results for GNN-based vulnerability injection approach (Graph2Edit, **corresponding to the experiments in RQ4**.
    - `scripts/githubedits/`: The scripts to start training and testing the Graph2Edit model.
    - `source_data/githubedits/`: The training, validation, and testing data for Graph2Edit.
    - `exp_githubedits_runs/`: The training and testing outputs for Graph2Edit, including the manual inspection results (**corresponding to Table 1 Row 5 (Graph2Edit)**).
- `devign/`: The source code, evaluation data, and results for DL-based vulnerability detection approach Devign (**corresponding to the results in Table 2 Tool Devign**).
    - `models/`: The saved models for each experiment.
    - `*.sh`: The script to start the experiment in each setting.
    - `*.txt`: The experiment result in each setting.
    - `*.json.shard*`: The evaluation data in each setting.
- `reveal/`: The source code, evaluation data, and results for DL-based vulnerability detection approach ReVeal (**corresponding to the results in Table 2 Tool ReVeal**).
    - `*_api_test.py`: The script to start the experiment in each setting.
    - `*.txt`: The experiment result in each setting.
    - `*.pt`: The saved models for each experiment.
    - `*.json`: The evaluation data in each setting.

## How to use

Please use the bold text in the package structure to find the source code, evaluation data, and results for the corresponding contents described in the original paper. For example, the dataset described in **Section V.B** is stored in `pattern_mining_applying/VulGen_beam_1/VulDatasets`. The raw output for the experiment in **Table 1 Row 2 (VulGen) Column 2 (Precision)** is stored in `pattern_mining_applying/VulGen_beam_1/res.txt`. To reproduce the experiments, please refer to the scripts (`*.sh` or `*.py`) described in the package structure to run the experiments. 




