from IPython.core.display import HTML


def pass_html():
    return HTML(
        """
        <div class='test_pass'>
            <strong>Success:</strong> Good job!
        </div>
        """
    )


def fail_html(msg=""):
    return HTML(
        """
        <div class='test_fail'>
            <strong>Failure:</strong> %s
        </div>
        """ % (msg, )
    )
